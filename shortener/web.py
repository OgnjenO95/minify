from base.application.components import Base
from base.application.components import api
from base.application.components import params
from base.application.components import authenticated, db

from src.models.user import Minify

languages = [
    {'id': 'de', 'text': 'german'},
    {'id': 'it', 'text': 'italian'},
    {'id': 'en', 'text': 'english'}
]


@api(
    URI=['/?', '/:__LANG__/?'],
    PREFIX=None
)
@authenticated(
    authentication_level='WEAK',
)
@db()
class Index(Base):
    @params(
        {'name': 'language', 'type': str, 'doc': 'language', 'required': False, 'default': 'de'},
        # {'name': 'id_url', 'type': int, 'doc': 'id', 'required': False},
    )
    def get(self, lang, **kwargs):
        ulang = '/' + lang + '/' '' if lang != 'en' and lang else '/'

        urls = self.orm_session.query(Minify).all()

        self.render('templates/index.html',  url='/', urls=urls)
