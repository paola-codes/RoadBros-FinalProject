"""empty message

Revision ID: 8d9dfb1df2c1
Revises: e85ebba547c2
Create Date: 2021-11-30 01:01:07.703472

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8d9dfb1df2c1'
down_revision = 'e85ebba547c2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('request', sa.Column('vehicle', sa.String(length=450), nullable=True))
    op.drop_constraint('request_vehicle_id_fkey', 'request', type_='foreignkey')
    op.drop_column('request', 'vehicle_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('request', sa.Column('vehicle_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('request_vehicle_id_fkey', 'request', 'vehicle', ['vehicle_id'], ['id'])
    op.drop_column('request', 'vehicle')
    # ### end Alembic commands ###
