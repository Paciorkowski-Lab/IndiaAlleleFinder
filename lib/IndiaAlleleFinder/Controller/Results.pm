package IndiaAlleleFinder::Controller::Results;
use Moose;
use namespace::autoclean;
use Scalar::Util qw(looks_like_number);

BEGIN { extends 'Catalyst::Controller'; }

=head1 NAME

IndiaAlleleFinder::Controller::Results - Catalyst Controller

=head1 DESCRIPTION

Catalyst Controller.

=head1 METHODS

=cut


=head2 index

=cut

sub index :Path :Args(0) {
    my ( $self, $c ) = @_;
    #$c->response->body('Matched IndiaAlleleFinder::Controller::Results in Results.');
 	#$c->stash(genes => [$c->model('IndiaAlleleFinderDB::Allele')->all]);
	
	my $query = $c->request->param('search');
	#$c->stash->{genes} = $query; #show everything
	my $variantQuery = "ayyy";

	#search by gene
	$c->stash(genes => 
		[$c->model('IndiaAlleleFinderDB::Allele')->search({generefgene => {'like', "$query"}})]);

	# #search by rsID
	# $c->stash(rsID => 
	# 	[$c->model('IndiaAlleleFinderDB::Allele')->search({snp138 => {'like', "$query"}})]);
	

	#search by variant: 12-53701241-G-A
	my ($chromosome, $pos, $ref, $alt) = split(/-/, $query);
	if ((looks_like_number($chromosome) or $chromosome eq 'X' or $chromosome eq 'Y') and 
		$pos ne '' and $ref ne '' and $alt ne '') {
		#we have a valid variant query.
		$variantQuery = "yooo";
		$c->stash(variantQuery => $variantQuery);

		$c->stash(genes => 
			[$c->model('IndiaAlleleFinderDB::Allele')->search({
				chr => {'like', "$chromosome"}, 
				start => {'like', "$pos"},
				ref => {'like', "$ref"},
				alt => {'like', "$alt"}
				})]);
	}
	
	#search by region
	#12:53701240-53701242
	($chromosome, my $region) = split(/:/, $query);
	my ($start, $end) = split(/-/, $region);
	if ((looks_like_number($chromosome) or $chromosome eq 'X' or $chromosome eq 'Y') 
		and looks_like_number($start) and looks_like_number($end)) {
		$c->stash(genes => [$c->model('IndiaAlleleFinderDB::Allele')->search({
			chr => {'like', "$chromosome"},
			start => {">=" => "$start", 
						"<=" => "$end"}
			})]);
	}

	$c->stash(searchText => $query);
	$c->stash(template => 'results.tt');

	#ghetto debugging here we go
	# $c->stash(chr => $chromosome);
	# $c->stash(region => $pos);
	# $c->stash(variantQuery => $variantQuery);
}

=head3 list

Fetch all results objects, pass to books/list.tt in stash to be displayed

=cut

sub list :Local :Arg(0) {
	my ($self, $c) = @_;

	#print $c->request->arguments->[0];
	
	my $query = $c->request->param('search');

	$c->stash->{genes} = 'query';
	$c->stash(template => 'results.tt');
}
=encoding utf8

=head1 AUTHOR

Jimmy Zhang

=head1 LICENSE

This library is free software. You can redistribute it and/or modify
it under the same terms as Perl itself.

=cut

__PACKAGE__->meta->make_immutable;

1;
