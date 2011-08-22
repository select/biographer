# Copyright (c) 2011, Thomas Handorf, The Biographer Community

# This file is part of Biographer.
# 
# Biographer is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# Biographer is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU Lesser General Public License
# along with Biographer.  If not, see <http://www.gnu.org/licenses/>.

use SGraph;
use SGraph::Dot;
use Data::Dumper;
use strict;

die "no input data" unless -f $ARGV[0];
die "no output data" unless -f $ARGV[1];

my $g=new SGraph;


# read input format
my $fh;
open($fh,"<",$ARGV[0]);
my @lines=split(/\n/,join('',<$fh>));
close $fh;
my $l='';
while (!($l=~/^\//)) {$l=shift(@lines)} #skip compartments

shift(@lines); # number of nodes;

my $nodes=[];
my $nidx=shift(@lines);

while (scalar(@lines) && (!($nidx=~/^\//))){
   my $type=shift(@lines);
   my $id=shift(@lines);
#   print "$id\n";
   shift(@lines);# compartment
   my $x=shift(@lines);
   my $y=shift(@lines);
#   $x*=72;
#   $y*=72;
   my $w=shift(@lines)/72; # w
   my $h=shift(@lines)/72; # h
   shift(@lines); # dir;
   $g->add_node($id,{pos=>"$x,$y!",width=>$w,height=>$h,shape=>"rect",fixedsize=>"true"});
   $nodes->[$nidx]=$id;
   $nidx=shift(@lines) # next index;
}

our $arrowshapes={Product=>"normal",Substrate=>"normal",Catalyst=>"odot",Activator=>"onormal",Inhbitor=>"tee"};


shift(@lines); #skip first index

while (scalar(@lines)){
   my $l=shift(@lines);
   my ($type,$from,$to)=split(" ",$l);
   if ($type eq 'Product') {
      my $h=$from;$from=$to;$to=$h;
   }
   $g->add_edge($nodes->[$from],$nodes->[$to],{arrowhead=>$arrowshapes->{$type}});
}

#read output format
$fh;
open($fh,"<",$ARGV[1]);
@lines=split(/\n/,join('',<$fh>));
close $fh;

shift(@lines); #skip first index
while (scalar(@lines)){
   my $type=shift(@lines);
   my $id=shift(@lines);
#   print "$id\n";
   shift(@lines);# compartment
   my $x=shift(@lines);
   my $y=shift(@lines);
#   $x*=72;
#   $y*=72;
   $g->set_attribute($id,"pos","$x,$y!");
   shift(@lines); # w
   shift(@lines); # h
   shift(@lines); # dir;
   shift(@lines) if scalar(@lines); # next index;
}

my $fn=$ARGV[0];
$fn=$ARGV[2] if $ARGV[2]; # third argument maybe output png file
$fn=~s/\.[^\.]*$//; # remove extension

print $g->dot;
#open($f,"| tee $fn.lyt.dot | neato -n -Gpad=0 -Gmargin=0 -Gsplines=true -Gdpi=56 -Tpng -o $fn.png");
my $f;
open($f,"| neato -n -Gpad=0 -Gmargin=0 -Gsplines=true -Gdpi=56 -Tpng -o $fn.png");
print $f $g->dot;
close $f;
