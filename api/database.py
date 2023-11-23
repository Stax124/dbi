from sqlmodel import SQLModel, create_engine


def create_connection(debug: bool = False):
    sqlite_file_name = "db.sqlite"
    sqlite_url = f"sqlite:///{sqlite_file_name}"

    engine = create_engine(sqlite_url, echo=debug)
    return engine


def create_metadata():
    from api.models.article import Article
    from api.models.user import User

    connection = create_connection()

    metadata = SQLModel.metadata
    metadata.create_all(connection)
    return metadata


def create_session():
    from sqlmodel import Session

    connection = create_connection()
    session = Session(connection)
    return session


def create_default_user():
    from api.models.user import User

    session = create_session()

    if session.query(User).first():
        return

    admin = User(
        username="admin",
        password="rootroot",
        email="test@gmail.com",
    )

    session.add(admin)
    session.commit()
