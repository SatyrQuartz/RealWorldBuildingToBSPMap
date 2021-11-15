rm out.pts
rm out.map
rm out.log
rm out.bsp

7z -y e 01_algodoo_file/map.phz scene.phn
mkdir 02_parse
mv scene.phn 02_parse
cat './02_parse/scene.phn' | grep -E -- 'addBox|pos |color |size |angle ' > ./02_parse/tempfile.txt
sed -i "s% := %=%g" ./02_parse/tempfile.txt
hexdump -ve '1/1 "%.2X"' ./02_parse/tempfile.txt | \
                sed "s/5D3B/22/g" | \
                xxd -r -p > tempfile.tmp
                mv tempfile.tmp ./02_parse/tempfile.txt
hexdump -ve '1/1 "%.2X"' ./02_parse/tempfile.txt | \
                sed "s/3B/22/g" | \
                xxd -r -p > tempfile.tmp
                mv tempfile.tmp ./02_parse/tempfile.txt
hexdump -ve '1/1 "%.2X"' ./02_parse/tempfile.txt | \
                sed "s/616E676C653D/616E676C653D22/g" | \
                xxd -r -p > tempfile.tmp
                mv tempfile.tmp ./02_parse/tempfile.txt
hexdump -ve '1/1 "%.2X"' ./02_parse/tempfile.txt | \
                sed "s/3D5B/3D22/g" | \
                xxd -r -p > tempfile.tmp
                mv tempfile.tmp ./02_parse/tempfile.txt
sed -i "s%, %,%g" ./02_parse/tempfile.txt

sed -i "s%Scene.addBox {%makecube%g" ./02_parse/tempfile.txt

cat ./03_conversion/phuntomapscript.sh ./02_parse/tempfile.txt > ./03_conversion/finalbuild.sh
chmod +x ./03_conversion/finalbuild.sh

rm out.map
echo "// Game: Generic" >> out.map
echo "// Format: Standard" >> out.map
echo "// entity 0" >> out.map
echo "{" >> out.map
echo '"classname" "worldspawn"' >> out.map
./03_conversion/finalbuild.sh
echo "}" >> out.map

echo "// entity 1" >> out.map
echo "{" >> out.map
echo '"classname" "info_player_start"' >> out.map
echo '"origin" "0 0 43"' >> out.map
echo "}" >> out.map

rm ./02_parse/tempfile.txt
rm ./02_parse/scene.phn
rm ./03_conversion/finalbuild.sh

/home/colbydray/.apps/mapcompile/quake-ericw/qbsp out.map
