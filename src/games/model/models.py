from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from migration.database import Base

class Game(Base):
    __tablename__ = "game"

    id = Column(Integer, index=True, primary_key=True)
    name = Column(String(200), nullable=False)
    creation_date = Column(DateTime, nullable=False, default=datetime.utcnow)
    modification_date = Column(DateTime, nullable=True)

    questions = relationship("Question", backref="game")


class Question(Base):
    __tablename__ = "question"

    id = Column(Integer, index=True, primary_key=True)
    question_text = Column(String(200), nullable=False)
    game_id = Column(Integer, ForeignKey("game.id"))
    creation_date = Column(DateTime, nullable=False, default=datetime.utcnow)

    choices = relationship("Choice", backref="question")


class Choice(Base):
    __tablename__ = "choice"

    id = Column(Integer, index=True, primary_key=True)
    choice_text = Column(String(200), nullable=False)
    question_id = Column(Integer, ForeignKey("question.id"))