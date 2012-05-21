#!/usr/bin/env perl

use Time::HiRes;

my $start;
my $end;
my $delta;

for (1 .. 1000) {
    my @rand = map { rand } (1..1_000_000);

    $start = Time::HiRes::time();
    # without the 'spaceship operator' it does an alpha sort
    my @sorted = sort {$a <=> $b} @rand;  # wat
    $end = Time::HiRes::time();

    $delta = ($end - $start) * 1000000;
    print "Elapsed time $delta\n";
}
