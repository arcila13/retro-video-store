"""empty message

Revision ID: 1727638f61fc
Revises: 460ed8d333a7
Create Date: 2021-11-10 22:49:08.699702

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1727638f61fc'
down_revision = '460ed8d333a7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('rental', sa.Column('customer_id', sa.Integer(), nullable=False))
    op.add_column('rental', sa.Column('due_date', sa.DateTime(), nullable=True))
    op.add_column('rental', sa.Column('video_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'rental', 'customer', ['customer_id'], ['id'])
    op.create_foreign_key(None, 'rental', 'video', ['video_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'rental', type_='foreignkey')
    op.drop_constraint(None, 'rental', type_='foreignkey')
    op.drop_column('rental', 'video_id')
    op.drop_column('rental', 'due_date')
    op.drop_column('rental', 'customer_id')
    # ### end Alembic commands ###
