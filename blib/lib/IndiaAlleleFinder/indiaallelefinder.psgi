use strict;
use warnings;

use IndiaAlleleFinder;

my $app = IndiaAlleleFinder->apply_default_middlewares(IndiaAlleleFinder->psgi_app);
$app;

