class Article:

    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.append(self)
    
    def __getitem__(self, index):
        if index == 0:
            return self.author
        elif index == 1:
            return self.magazine
        elif index == 2:
            return self.title

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
    
    # def get_author(self):
    #     return self.author

    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, value):

        self._magazine = value
        return self._magazine
    
    # def magazine(self):
    #     for each in Magazine.all:
    #         if self.magazine == each:
    #             return each
    
    @classmethod
    def append(cls, article):
        cls.all.append(article)
        
class Author:

    all = []

    def __init__(self, name):
        self.name = name
        Author.append(self)

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
    
    @classmethod
    def append(cls, author):
        cls.all.append(author)

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other

    def articles(self):
        article_list = []

        for article in Article.all:
            if self.name == article[0]:
                article_list.append(article)
        return article_list

    def magazines(self):
        article_list = []

        for article in Article.all:
            if self.name == article[0]:
                article_list.append(article)
        
        magazine_list = []

        for article in article_list:
            magazine_list.append(article[1])
       
        unique_magazine_list = []

        for magazine in magazine_list:
            if magazine not in unique_magazine_list:
                unique_magazine_list.append(magazine)
            else:
                pass
        
        return unique_magazine_list

    def add_article(self, magazine, title):
        new_article = Article(self.name, magazine, title)
        return new_article

    def topic_areas(self):
        magazine_list = []

        for article in Article.all:
            if self.name == article[0]:
                magazine_list.append(article[1])
        
        unique_magazines = []

        for each in magazine_list:
            if each not in unique_magazines:
                unique_magazines.append(each)

        unique_categories = []

        for each in unique_magazines:
            unique_categories.append(each[1])

        if unique_categories == []:
            return None
        else:
            return unique_categories

class Magazine:

    all = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.append(self)
    
    def __getitem__(self, index):
        if index == 0:
            return self.name
        elif index == 1:
            return self.category
    
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
    
    @classmethod
    def append(cls, magazine):
        cls.all.append(magazine)
    
    def articles(self):
        article_list = []

        for article in Article.all:
            if self.name == article[1][0]:
                article_list.append(article)
        
        return article_list

    def contributors(self):
        article_list = []

        for article in Article.all:
            if self.name == article[1][0]:
                article_list.append(article)
        
        author_list = []

        for article in article_list:
            author_list.append(article[0])
        
        unique_author_list = []

        for author in author_list:
            if author not in unique_author_list:
                unique_author_list.append(author)
        
        return unique_author_list

    def article_titles(self):
        article_title_list = []

        for article in Article.all:
            if self.name == article[1][0]:
                article_title_list.append(article[2])

        if article_title_list == []:
            return None
        else:    
            return article_title_list

    def contributing_authors(self):
        pass