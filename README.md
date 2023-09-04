OpenTrackr provides a list of infohashes for each takedown request it receives. [Link](https://opentrackr.org/transparency.html)

This project takes those lists and matches each infohash to a human readable title.

Titles are sourced from the Kiwi Torrent Research sqlite dataset. [Link](https://github.com/Kiwi-Torrent-Research/Kiwi-Torrent-Research)

Requirements:
 - Python 3
 - Kiwi Torrent Research sqlite dataset (any version)

Instructions:
 - Set the DATABASE variable in opentrackr_transparency.py to your dataset filename ('dump_30_08_2023.sqlite' by default)
 - Run opentrackr_transparency.py

See [out.txt](https://raw.githubusercontent.com/Kiwi-Torrent-Research/OpenTrackr-Takedown-Transparency/main/out.txt) for the output of this program (run on 04/09/2023 using 30/08/2023 dataset).
