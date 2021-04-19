"""empty message

Revision ID: 0d4f9ca69102
Revises: 05b5ee13afa9
Create Date: 2021-04-18 16:31:38.692187

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0d4f9ca69102'
down_revision = '05b5ee13afa9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('files', sa.Column('uploaded_on', sa.DateTime(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('files', 'uploaded_on')
    # ### end Alembic commands ###