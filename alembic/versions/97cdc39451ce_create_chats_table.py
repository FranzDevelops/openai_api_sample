"""create chats table

Revision ID: 97cdc39451ce
Revises: 
Create Date: 2023-05-17 23:04:43.545200

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '97cdc39451ce'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'chats',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('message', sa.String(length=255), nullable=True),
        sa.Column('response', sa.String(length=255), nullable=True),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()')),
    )
    pass


def downgrade() -> None:
    op.drop_table('chats')
    pass
