#!/usr/bin/env bash
#
# Geographic distrubtions of group members' hometown.
#
gmt begin seismolab-members png
    gmt set MAP_GRID_PEN_PRIMARY 0.25p,gray,2_2
    # Plot the China region
    gmt coast -JM105/35/10c -R70/138/13/56 -Ba10f5g10 -B+t"Tian's Seismolab Members" -G244/243/239 -S167/194/223
    gmt basemap -Lg85/17.5+c17.5+w800k+f+u --FONT_ANNOT_PRIMARY=4p
    gmt plot CN-border-La.gmt -W0.1p

    gmt inset begin -DjRB+w1.8c/2.2c -F+p0.5p
        gmt coast -JM? -R105/123/3/24 -G244/243/239 -S167/194/223 -Df
        gmt plot CN-border-La.gmt -W0.1p
    gmt inset end

	gmt plot -St0.1c -Gblack <<- EOF
	117.02 32.59  # Huainan
	104.07 30.66  # Chengdu
	114.48 36.61  # Handan
	105.82 32.45  # Guangyuan
	114.41 30.52  # Wuhan
	EOF
	echo 114.41 30.52 | gmt plot -Sa0.2c -Gred -t50
gmt end show
