from elasticsearch_dsl.connections import connections
from django_elasticsearch_dsl import DocType, Index
from .models import Mail

# Create a connection to ElasticSearch
connections.create_connection()

mail = Index('mails')

# reference elasticsearch doc for default settings here
mail.settings(
    number_of_shards=1,
    number_of_replicas=0
)

@mail.doc_type
class MailDocument(DocType):

    class Meta:
        model = Mail
        fields = ['rec_id', 'bcc', 'cc','sub','message','csv','mail_time']
