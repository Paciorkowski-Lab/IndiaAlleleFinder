package IndiaAlleleFinder::Controller::Results;
use Moose;
use namespace::autoclean;

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

    $c->response->body('Matched IndiaAlleleFinder::Controller::Results in Results.');
}

=head3 list

Fetch all results objects, pass to books/list.tt in stash to be displayed

=cut

sub list :Local {
	my ($self, $c) = @_;

	$c->stash(genes => [$c->model('IndiaAlleleFinderDB::Allele')->all]);

	$c->stash(template => 'list.tt');
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
