"""empty message

Revision ID: 6210d40a10c8
Revises: 9ddee605c913
Create Date: 2019-11-23 13:05:51.592901

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6210d40a10c8'
down_revision = '9ddee605c913'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('avatar_hash', sa.String(length=32), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'avatar_hash')
    # ### end Alembic commands ###
