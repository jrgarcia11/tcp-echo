gnome-terminal -e "bash -c \"echo I AM THE SERVER; python tcpServerFileTrans.py; exec bash\""
gnome-terminal -e "bash -c \"echo I AM THE PROXY; python stutter-forwarder.py localhost:50006 localhost:50007; exec bash\""
gnome-terminal -e "bash -c \"echo I AM THE CLIENT; python tcpClientFileTrans.py; exec bash\""
