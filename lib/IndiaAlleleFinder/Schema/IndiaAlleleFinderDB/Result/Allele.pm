use utf8;
package IndiaAlleleFinder::Schema::IndiaAlleleFinderDB::Result::Allele;

# Created by DBIx::Class::Schema::Loader
# DO NOT MODIFY THE FIRST PART OF THIS FILE

=head1 NAME

IndiaAlleleFinder::Schema::IndiaAlleleFinderDB::Result::Allele

=cut

use strict;
use warnings;

use Moose;
use MooseX::NonMoose;
use MooseX::MarkAsMethods autoclean => 1;
extends 'DBIx::Class::Core';

=head1 COMPONENTS LOADED

=over 4

=item * L<DBIx::Class::InflateColumn::DateTime>

=back

=cut

__PACKAGE__->load_components("InflateColumn::DateTime");

=head1 TABLE: C<alleles>

=cut

__PACKAGE__->table("alleles");

=head1 ACCESSORS

=head2 chr

  data_type: 'text'
  is_nullable: 1

=head2 start

  data_type: 'text'
  is_nullable: 1

=head2 end

  data_type: 'text'
  is_nullable: 1

=head2 ref

  data_type: 'text'
  is_nullable: 1

=head2 alt

  data_type: 'text'
  is_nullable: 1

=head2 funcrefgene

  data_type: 'text'
  is_nullable: 1

=head2 generefgene

  data_type: 'text'
  is_nullable: 1

=head2 exonicfuncrefgene

  data_type: 'text'
  is_nullable: 1

=head2 aachangerefgene

  data_type: 'text'
  is_nullable: 1

=head2 phastconselements46way

  data_type: 'text'
  is_nullable: 1

=head2 genomicsuperdups

  data_type: 'text'
  is_nullable: 1

=head2 snp138

  data_type: 'text'
  is_nullable: 1

=head2 hummusphastconschr

  data_type: 'text'
  is_nullable: 1

=head2 primatesphastconschr

  data_type: 'text'
  is_nullable: 1

=head2 hummusvistachr

  data_type: 'text'
  is_nullable: 1

=head2 indiafreq

  data_type: 'text'
  is_nullable: 1

=head2 otherinfo

  data_type: 'text'
  is_nullable: 1

=cut

__PACKAGE__->add_columns(
  "chr",
  { data_type => "text", is_nullable => 1 },
  "start",
  { data_type => "text", is_nullable => 1 },
  "end",
  { data_type => "text", is_nullable => 1 },
  "ref",
  { data_type => "text", is_nullable => 1 },
  "alt",
  { data_type => "text", is_nullable => 1 },
  "funcrefgene",
  { data_type => "text", is_nullable => 1 },
  "generefgene",
  { data_type => "text", is_nullable => 1 },
  "exonicfuncrefgene",
  { data_type => "text", is_nullable => 1 },
  "aachangerefgene",
  { data_type => "text", is_nullable => 1 },
  "phastconselements46way",
  { data_type => "text", is_nullable => 1 },
  "genomicsuperdups",
  { data_type => "text", is_nullable => 1 },
  "snp138",
  { data_type => "text", is_nullable => 1 },
  "hummusphastconschr",
  { data_type => "text", is_nullable => 1 },
  "primatesphastconschr",
  { data_type => "text", is_nullable => 1 },
  "hummusvistachr",
  { data_type => "text", is_nullable => 1 },
  "indiafreq",
  { data_type => "text", is_nullable => 1 },
  "otherinfo",
  { data_type => "text", is_nullable => 1 },
);


# Created by DBIx::Class::Schema::Loader v0.07043 @ 2015-11-10 19:37:13
# DO NOT MODIFY THIS OR ANYTHING ABOVE! md5sum:+vOLnrxpRDO9lkql2OW2Iw


# You can replace this text with custom code or comments, and it will be preserved on regeneration
__PACKAGE__->meta->make_immutable;
1;
