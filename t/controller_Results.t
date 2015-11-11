use strict;
use warnings;
use Test::More;


use Catalyst::Test 'IndiaAlleleFinder';
use IndiaAlleleFinder::Controller::Results;

ok( request('/results')->is_success, 'Request should succeed' );
done_testing();
