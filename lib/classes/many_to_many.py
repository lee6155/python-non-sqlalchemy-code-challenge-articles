class Article:

    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

    def __repr__(self):
        return f"{self.author, self.magazine, self.title}"

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title (self, value):
        if type(value) != str:
            raise TypeError("Title must be a string")
        if len(value) < 5 or len(value) > 50:
            raise ValueError("Title must be between 5 and 50 characters")
        if hasattr(self, '_title'):
            raise AttributeError("This attribute is immutable")
        
        self._title = value
        return self._title
    
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):

        self._author = value
        return self._author

    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, value):

        self._magazine = value
        return self._magazine
        
class Author:

    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def __repr__(self):
        return f"'{self.name}'"

    @property
    def name (self):
        return self._name
    
    @name.setter
    def name (self, value):
        if type(value) != str:
            raise TypeError("Name must be a string")
        if len(value) == 0:
            raise ValueError("Name must longer than 0 characters")
        if hasattr(self, '_name'):
            raise AttributeError("This attribute is immutable")
        
        self._name = value
        return self._name

    def articles(self):
        return [article for article in Article.all if self == article.author]

    def magazines(self):
        articles_by_author = [article for article in Article.all if self == article.author]

        magazines = [article.magazine for article in articles_by_author]
       
        unique_magazines = []
        
        for magazine in magazines:
            if magazine not in unique_magazines:
                unique_magazines.append(magazine)
            else:
                pass
        
        return unique_magazines

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        magazines_by_author = [article.magazine for article in Article.all if self == article.author]
        
        magazine_categories = [magazine.category for magazine in magazines_by_author]

        unique_magazine_categories = []

        for category in magazine_categories:
            if category not in unique_magazine_categories:
                unique_magazine_categories.append(category)
            else:
                pass

        if unique_magazine_categories == []:
            return None
        else:
            return unique_magazine_categories

class Magazine:

    all = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all.append(self)
    
    def __repr__(self):
        return f"{self.name, self.category}"

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if type(value) != str:
            raise TypeError("Name must be a string")
        if len(value) < 2 or len(value) > 16:
            raise ValueError("Name must be between 2 and 16 characters")

        self._name = value
        return self._name
    
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value):
        if type(value) != str:
            raise TypeError("Category must be a string")
        if len(value) == 0:
            raise ValueError("Category must be longer than 0 characters")
        
        self._category = value
        return self._category
    
    def articles(self):
        return [article for article in Article.all if self == article.magazine]

    def contributors(self):
        authors_for_magazine = [article.author for article in Article.all if self == article.magazine]

        unique_author_list = []

        for author in authors_for_magazine:
            if author not in unique_author_list:
                unique_author_list.append(author)
            else:
                pass
        
        return unique_author_list

    def article_titles(self):
        article_titles = [article.title for article in Article.all if self == article.magazine]

        if article_titles == []:
            return None
        else:    
            return article_titles

    def contributing_authors(self):
        authors_for_magazine = [article.author for article in Article.all if self == article.magazine]
        
        unique_authors = []

        for author in authors_for_magazine:
            if author not in unique_authors:
                unique_authors.append(author)
        
        unique_authors_article_count = {}

        for author in unique_authors:
            unique_authors_article_count[author] = authors_for_magazine.count(author)

        authors_two_plus_articles = []

        for author in unique_authors_article_count:
            if unique_authors_article_count[author] > 2:
                authors_two_plus_articles.append(author)

        if authors_two_plus_articles == []:
            return None
        else:
            return authors_two_plus_articles
