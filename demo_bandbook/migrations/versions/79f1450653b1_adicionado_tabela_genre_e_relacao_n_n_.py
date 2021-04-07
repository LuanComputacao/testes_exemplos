"""adicionado tabela genre e relacao n:n de genres com bands

Revision ID: 79f1450653b1
Revises: a50064668bdf
Create Date: 2021-04-06 09:57:20.412677

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '79f1450653b1'
down_revision = 'a50064668bdf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('genres',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('band_genres',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('band_id', sa.Integer(), nullable=True),
    sa.Column('genre_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['band_id'], ['bands.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['genre_id'], ['genres.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('band_genres')
    op.drop_table('genres')
    # ### end Alembic commands ###