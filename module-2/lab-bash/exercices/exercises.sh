echo "Hello world"
mkdir new_dir
rm -r new_dir
cp lorem/sed.txt lorem-copy
cp lorem/at.txt lorem/lorem.txt lorem-copy
cat lorem/sed.txt
cat lorem/at.txt lorem/lorem.txt
cat lorem-copy/sed.txt | head -n 3
cat lorem-copy/sed.txt | tail -n 3
echo "Homo homini lupus" >> lorem-copy/sed.txt 
cat lorem-copy/sed.txt | head -n 3
sed -i 's/et/ET/g' lorem-copy/at.txt # -i: inplace, g: global
whoami
pwd
ls lorem/*.txt
wc -l lorem/sed.txt
ls -R | grep -c "^lorem\." # -R: list recursively, ^: start by
cat lorem/at.txt | grep -o "et" | wc -l 
# -o:  Print only the matched parts of a matching line, with each such part on a separate output line
grep -ro "et" lorem-copy | wc -l # -r: grep recursively in the specified directory