from base.application.components import Base
from base.application.components import api
from base.application.components import params
from base.application.components import db
import requests
import json
import hashlib
from hashlib import md5
import src.models.user as models
from urllib.parse import urlparse

@api(
    URI='/shorten-url',
)
class ShortenUrlHandler(Base):

    @params(
        {'name': 'url', 'type': str, 'doc': 'Ovde prihvatamo dugacak URL da bismo ga ubacili u bazu.', 'required': True},
    )
    @db()
    def put(self, url):
        '''
            dodavanje novog dugackog url-a da bismo ga skratili
        '''
        if url == '':
            return self.error("Nema linka")

        # elif urlparse(url)[0] == '':
        #     return self.error("Los link")
        elif requests.get(url).status_code == '<Response [200]>':
            return self.error("Los link")
        else:
            result = self.orm_session.query(models.Minify).filter(models.Minify.url == url).one_or_none()
            if result:
                return self.ok(result.short_url)
            else:
                shortenUrl = hashlib.md5(url.encode('utf-8')).hexdigest()
                shortenUrl = f'{shortenUrl[:7]}'

                objekatMinify = models.Minify(url, shortenUrl)
                self.orm_session.add(objekatMinify)

                try:
                    self.orm_session.commit()
                except Exception as e:
                    self.orm_session.rollback()
                    return self.error(f"Nesto je poslo po zlu, pokusajte kasnije: {e}")

                return self.ok(shortenUrl)

@api(
    URI='/url/:custom'
)
class GetUrlHandler(Base):

    @params(
        {'name': 'custom', 'type': str, 'doc': 'Ovde uzimamo URL iz baze prema prosledjenom URL-u.', 'required': True},
    )
    @db()
    def get(self, custom):
        '''
           vracanje url-a iz baze
        '''
        long_url = self.orm_session.query(models.Minify.url).filter(custom == models.Minify.short_url).one_or_none()

        response = requests.get(long_url[0])

        return self.ok(response.url)


