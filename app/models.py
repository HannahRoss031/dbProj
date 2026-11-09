import sqlalchemy as sa
from app import db

''' User Tables '''
class User(db.Model):
    __tablename__ = 'users' # explicit tablename

    userId: Mapped[int] = sa.Column(primary_key=True)
    username: Mapped[str] = sa.Column(sa.String(64), index=True,
                                                unique=True)
    password_hash: Mapped[Optional[str]] = sa.Column(sa.String(256))

    # specification for debugging purposes - shows the username in the representation
    def __repr__(self):
        return '<User {}>'.format(self.username)

class UserHistory(db.Model):
    __tablename__ = 'user_history' # explicit tablename

    historyId: Mapped[int] = sa.Column(primary_key=True)
    userId: Mapped[int] = sa.Column(sa.ForeignKey('users.userId'))
    action: Mapped[str] = sa.Column(sa.String(256))
    timestamp: Mapped[datetime] = sa.Column(sa.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<UserHistory {}>'.format(self.action)
