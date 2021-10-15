tail -n 10 pumps.log > pumps1.log
mv pumps1.log pumps.log
sudo systemctl stop pumps
sudo systemctl disable pumps
sudo systemctl daemon-reload
sudo systemctl enable pumps
sudo systemctl start pumps
sudo systemctl status pumps