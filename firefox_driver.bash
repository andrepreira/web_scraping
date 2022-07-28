RUN	wget -qO- https://github.com/mozilla/geckodriver/releases/download/v0.31.0/geckodriver-v0.31.0-linux64.tar.gz \
		| tar -zxOf - > /usr/local/bin/geckodriver \
		&& chmod +x /usr/local/bin/geckodriver \
		&& apt update \
		&& apt install firefox-esr -y