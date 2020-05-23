"""empty message

Revision ID: b901766539b1
Revises: 6051c989902f
Create Date: 2020-05-12 01:30:04.106245

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b901766539b1'
down_revision = '6051c989902f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('seeking_talent', sa.Boolean(), nullable=True))
    op.add_column('Artist', sa.Column('seeking_venue', sa.String(length=500), nullable=True))
    op.drop_column('Artist', 'seeking_description')
    op.add_column('Venue', sa.Column('seeking_talent', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Venue', 'seeking_talent')
    op.add_column('Artist', sa.Column('seeking_description', sa.VARCHAR(length=500), autoincrement=False, nullable=True))
    op.drop_column('Artist', 'seeking_venue')
    op.drop_column('Artist', 'seeking_talent')
    # ### end Alembic commands ###