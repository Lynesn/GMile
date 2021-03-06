"""empty message

Revision ID: adcadb683647
Revises: 59b8aac7c61c
Create Date: 2019-08-30 15:48:57.954927

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'adcadb683647'
down_revision = '59b8aac7c61c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('loaders',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=60), nullable=True),
    sa.Column('username', sa.String(length=60), nullable=True),
    sa.Column('first_name', sa.String(length=60), nullable=True),
    sa.Column('last_name', sa.String(length=60), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('department_id', sa.Integer(), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.Column('is_admin', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['department_id'], ['departments.id'], ),
    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_loaders_email'), 'loaders', ['email'], unique=True)
    op.create_index(op.f('ix_loaders_first_name'), 'loaders', ['first_name'], unique=False)
    op.create_index(op.f('ix_loaders_last_name'), 'loaders', ['last_name'], unique=False)
    op.create_index(op.f('ix_loaders_username'), 'loaders', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_loaders_username'), table_name='loaders')
    op.drop_index(op.f('ix_loaders_last_name'), table_name='loaders')
    op.drop_index(op.f('ix_loaders_first_name'), table_name='loaders')
    op.drop_index(op.f('ix_loaders_email'), table_name='loaders')
    op.drop_table('loaders')
    # ### end Alembic commands ###
