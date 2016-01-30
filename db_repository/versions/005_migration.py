from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
listings = Table('listings', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('description', String(length=60)),
    Column('location', String(length=60)),
    Column('section', String(length=60)),
    Column('start_time', String(length=60)),
    Column('stop_time', String(length=60)),
    Column('subject', String(length=60)),
    Column('title', String(length=60)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['listings'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['listings'].drop()
