package IndiaAlleleFinder::Controller::Root;
use Moose;
use namespace::autoclean;

BEGIN { extends 'Catalyst::Controller' }

#
# Sets the actions in this controller to be registered with no prefix
# so they function identically to actions created in MyApp.pm
#
__PACKAGE__->config(namespace => '');

=encoding utf-8

=head1 NAME

IndiaAlleleFinder::Controller::Root - Root Controller for IndiaAlleleFinder

=head1 DESCRIPTION

[enter your description here]

=head1 METHODS

=head2 index

The root page (/)

=cut
sub chr :Path('chr') :Args {
	my ( $self, $c, $arg) = @_;
	my @chrom1 = ();
	my @chrom2 = ();
	my @chrom3 = ();
	my @chrom4 = ();
	my @chromxy = ();
	
	# my $i = 1;
	for (my $i = 1; $i < 23; $i++) {
		if ($i <= 6) {
			push @chrom1, $i;
		}
		if ($i > 6 and $i <= 12) {
			push @chrom2, $i;
		}
		if ($i > 12 and $i <= 18) {
			push @chrom3, $i;
		}
		if ($i > 18) {
			push @chrom4, $i;
		}	
	}
	push @chromxy, 'X';
	push @chromxy, 'Y';

	#[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22, "X","Y"]
	$c->stash(template => 'browseChr.tt', chrom1 => [@chrom1], chrom2 => [@chrom2], 
	chrom3 => [@chrom3], chrom4 => [@chrom4], chromxy => [@chromxy], arg => $arg); #assigning an array: variable => [@array]

	$c->stash(genes => [$c->model('IndiaAlleleFinderDB::Allele')->search({chr => {'like', "$arg"}})]);
}

sub sources :Path('sources.html') :Args(0) {
	my ( $self, $c) = @_;
	$c->stash(template => 'sources.tt', active_page => 'sources');
}

sub methods :Path('methods.html') :Args(0) {
	my ( $self, $c) = @_;
	$c->stash(template => 'methods.tt', active_page => 'methods');
}

sub gene :Global {
	my ( $self, $c) = @_;
	$c->stash(template => 'browseGene.tt');
} #might delete this.

sub index :Path :Args(0) {
	my ( $self, $c) = @_;
	my @chrom = ();

	for (my $i = 1; $i < 23; $i++) {
		push @chrom, $i;
	}
	push @chrom, 'X';
	push @chrom, 'Y';

	$c->stash(template => 'index.tt', searchText => 'type in a gene or variant', active_page => 'index', chrom => [@chrom]);
}

#sub index :Global {
#    my ( $self, $c ) = @_;

    # Hello World
    #$c->response->body( $c->welcome_message );
#	$c->stash(template => 'index.tt');
#}

=head2 default

Standard 404 error page

=cut

sub default :Path {
    my ( $self, $c ) = @_;
    $c->response->body( 'Page not found' );
    $c->response->status(404);
}

=head2 end

Attempt to render a view, if needed.

=cut

sub end : ActionClass('RenderView') {}

=head1 AUTHOR

Jimmy Zhang

=head1 LICENSE

This library is free software. You can redistribute it and/or modify
it under the same terms as Perl itself.

=cut

__PACKAGE__->meta->make_immutable;

1;
