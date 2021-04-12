cd sample
sudo mkdir /usr/bin/dirty

chmod a+x dirtyops.py
sudo mv *.py /usr/bin/dirty

curdir = pwd
cd /usr/bin
ln -s dirtyops /usr/bin/dirty/dirtyops.py

cd $curdir
echo "Installation done"
