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

my @chrom = ();
	
for (my $i = 1; $i < 23; $i++) {
	push @chrom, $i;
}
push @chrom, 'X';
push @chrom, 'Y';

sub chr :Path('chr') :Args {
	my ( $self, $c, $arg) = @_;

	#[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22, "X","Y"]
	$c->stash(template => 'browseChr.tt', active_page => 'browse', chrom => [@chrom], arg => $arg, searchText => 'type in a gene or variant'); #assigning an array: variable => [@array]

	$c->stash(genes => [$c->model('IndiaAlleleFinderDB::Allele')->search({chr => {'like', "$arg"}})]);
}

sub sources :Path('sources.html') :Args(0) {
	my ( $self, $c) = @_;
	$c->stash(template => 'sources.tt', active_page => 'sources', chrom => [@chrom]);
}

sub methods :Path('methods.html') :Args(0) {
	my ( $self, $c) = @_;
	$c->stash(template => 'methods.tt', active_page => 'methods', chrom => [@chrom]);
}

sub about :Path('about.html') :Args(0) {
	my ( $self, $c) = @_;
	$c->stash(template => 'about.tt', active_page => 'about', chrom => [@chrom]);
}

sub index :Path :Args(0) {
	my ( $self, $c) = @_;

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
