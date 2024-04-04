#!/usr/bin/env bash
# Script sets up servers for hosting web static files
# --------------------------------------------------------------------
#checks if nginx intalled
if  ! dpkg -s nginx &> /dev/null;
then
    sudo apt-get update
    sudo apt-get -y install nginx
    sudo ufw allow 'Nginx HTTP'
    sudo service nginx start
fi

# -----------------------------------------------------------
# check s if folder is present
dir="/data/"
dir2="/data/web_static/"
dir3="/data/web_static/releases/"
dir4="/data/web_static/shared/"
dir5="/data/web_static/releases/test/"

sudo mkdir -p "$dir" "$dir2" "$dir3" "$dir4" "$dir5"
# ----------------------------------------------------------
html="<html>
    <head>
        <title>ALX</title>
    </head>
    <body>
        <h1>Holberton School</h1>
    </body>
</html>"

echo "$html" | sudo tee  /data/web_static/releases/test/index.html
# ---------------------------------------------------------------------
#creates a symbolic link and deletes the link and recreate anytime script is ran
symlink="/data/web_static/current"
if [ ! -L "$symlink" ] && [ ! -e "$symlink" ];
then
    sudo ln -sf "$dir5" "$symlink"
else
    sudo rm "$symlink"
    sudo ln -sf "$dir5" "$symlink"
fi
# ------------------------------------------------
# changes ownership and group ownership to the user
user="ubuntu"
group="ubuntu"
sudo chown -hR "$user":"$group" "$dir"

# ------------------------------------------------
ADD_HBNBSTATIC="\\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n"
sudo sed -i "/server_name _;/a $ADD_HBNBSTATIC" /etc/nginx/sites-available/default
sudo service nginx restart
