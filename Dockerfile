FROM nginx:1.23.1

RUN apt -qq update \
    && apt -qq -y install --no-install-recommends fcgiwrap spawn-fcgi pandoc wkhtmltopdf unzip \
    && apt clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/share/fonts
RUN curl https://moji.or.jp/wp-content/ipafont/IPAexfont/IPAexfont00401.zip -O \
    && unzip IPAexfont00401.zip \
    && chmod a+r IPAexfont00401/*.ttf \
    && fc-cache -fv IPAexfont00401 \
    && rm -rf IPAexfont00401.zip

EXPOSE 80
STOPSIGNAL SIGTERM

COPY default.conf /etc/nginx/conf.d/

WORKDIR /usr/share/nginx
RUN mkdir -p cgi-bin/output \
    && chown -R nginx:nginx .
COPY index.cgi cgi-bin/
COPY template/ cgi-bin/template

COPY docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]
