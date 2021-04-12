cd sample
sudo mkdir /usr/bin/dirty

chmod a+x dirtyops.py
sudo mv *.py /usr/bin/dirty

cd /usr/bin
sudo ln -s /usr/bin/dirty/dirtyops.py dirtyops

echo "Installation done"
