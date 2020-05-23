"""empty message

Revision ID: 826fb752b69e
Revises: 938b87db8c26
Create Date: 2020-05-13 20:45:28.145579

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '826fb752b69e'
down_revision = '938b87db8c26'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('joinTable',
    sa.Column('Venue.id', sa.Integer(), nullable=False),
    sa.Column('Artist.id', sa.Integer(), nullable=False),
    sa.Column('start_time', sa.String(length=120), nullable=False),
    sa.Column('artist_name', sa.String(), nullable=False),
    sa.Column('venue_name', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['Artist.id'], ['Artist.id'], ),
    sa.ForeignKeyConstraint(['Venue.id'], ['Venue.id'], ),
    sa.PrimaryKeyConstraint('Venue.id', 'Artist.id', 'start_time', 'artist_name', 'venue_name')
    )
    op.drop_table('Show')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Show',
    sa.Column('start_time', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('artist_image_link', sa.VARCHAR(length=500), autoincrement=False, nullable=True),
    sa.Column('artist_name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('venue_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('artist_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('venue_name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['artist_id'], ['Artist.id'], name='Show_artist_id_fkey'),
    sa.ForeignKeyConstraint(['venue_id'], ['Venue.id'], name='Show_venue_id_fkey'),
    sa.PrimaryKeyConstraint('start_time', 'venue_id', 'artist_id', name='Show_pkey')
    )
    op.drop_table('joinTable')
    # ### end Alembic commands ###
