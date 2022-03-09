"""initdb

Revision ID: 12dba9ce674f
Revises: d4867f3a4c0a
Create Date: 2022-02-24 10:44:47.791881

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '12dba9ce674f'
down_revision = 'd4867f3a4c0a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('covid_status',
    sa.Column('ID', sa.Integer(), nullable=False),
    sa.Column('RU', sa.VARCHAR(length=255), nullable=True),
    sa.Column('KZ', sa.VARCHAR(length=255), nullable=True),
    sa.PrimaryKeyConstraint('ID')
    )
    op.create_index(op.f('ix_covid_status_ID'), 'covid_status', ['ID'], unique=False)
    op.create_table('covid_vacination',
    sa.Column('ID', sa.Integer(), nullable=False),
    sa.Column('VACCINATION_STATUS_ID', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['VACCINATION_STATUS_ID'], ['covid_status.ID'], ),
    sa.PrimaryKeyConstraint('ID')
    )
    op.create_index(op.f('ix_covid_vacination_ID'), 'covid_vacination', ['ID'], unique=False)
    op.alter_column('user', 'email',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('user', 'hashed_password',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'hashed_password',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('user', 'email',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.drop_index(op.f('ix_covid_vacination_ID'), table_name='covid_vacination')
    op.drop_table('covid_vacination')
    op.drop_index(op.f('ix_covid_status_ID'), table_name='covid_status')
    op.drop_table('covid_status')
    # ### end Alembic commands ###
