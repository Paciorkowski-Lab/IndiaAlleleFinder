package IndiaAlleleFinder::View::HTML;
use Moose;
use namespace::autoclean;

extends 'Catalyst::View::TT';

__PACKAGE__->config(
    TEMPLATE_EXTENSION => '.tt',
    render_die => 1,
);

=head1 NAME

IndiaAlleleFinder::View::HTML - TT View for IndiaAlleleFinder

=head1 DESCRIPTION

TT View for IndiaAlleleFinder.

=head1 SEE ALSO

L<IndiaAlleleFinder>

=head1 AUTHOR

Jimmy Zhang

=head1 LICENSE

This library is free software. You can redistribute it and/or modify
it under the same terms as Perl itself.

=cut

1;
