"""Add reset password fields

Revision ID: 18279714822f
Revises: 
Create Date: [날짜]

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '18279714822f'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('reset_token', sa.String(length=100), nullable=True))
        batch_op.add_column(sa.Column('reset_token_expiration', sa.DateTime(), nullable=True))
        batch_op.create_unique_constraint('uq_user_reset_token', ['reset_token'])

def downgrade():
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint('uq_user_reset_token', type_='unique')
        batch_op.drop_column('reset_token_expiration')
        batch_op.drop_column('reset_token')