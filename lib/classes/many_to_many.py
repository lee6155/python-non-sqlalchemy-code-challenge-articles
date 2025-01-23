class Article:

    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        self.append(author, magazine, title)

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
    
    @classmethod
    def append(cls, author, magazine, title):
        if (author, magazine, title) in cls.all:
            pass
        else:
            cls.all.append((author, magazine, title))
    
    def get_author(self):
        if self.author in Author.all:
            return self.author
        else:
            raise ValueError("Author must be an instance of the Author class")
    
    def get_magazine(self):
        for each in Magazine.all:
            if self.magazine in each:
                return each
            else:
                raise ValueError("Magazine must be an instance of the Magazine class")
        
class Author:

    all = []

    def __init__(self, name):
        self.name = name
        self.append(name)

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
    def append(cls, name):
        if name in cls.all:
            pass
        else:
            cls.all.append(name)

    def articles(self):
        article_list = []
        for article in Article.all:
            if self.name in article:
                article_list.append((article))
        return article_list

    def magazines(self):
        article_list = []

        for article in Article.all:
            if self.name in article:
                article_list.append(article)

        magazine_list = []

        for article in article_list:
            for magazine in Magazine.all:
                if article[1] in magazine:
                    magazine_list.append(magazine)

        unique_magazine_list = []

        for magazine in magazine_list:
            if magazine not in unique_magazine_list:
                unique_magazine_list.append(magazine)
            else:
                pass
        
        return unique_magazine_list

    def add_article(self, magazine, title):
        return(Article(self.name, magazine, title))

    def topic_areas(self):
        magazine_list = []

        for article in Article.all:
            if self.name in article:
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
        self.append(name, category)

    def __repr__(self):
        return f"{self.name, self.category}"
    
    def __getitem__(self, item):
        item = self.category
        return item

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
    def append(cls, name, category):
        if (name, category) in cls.all:
            pass
        else:
            cls.all.append((name, category))
    
    def articles(self):
        article_list = []

        for article in Article.all:
            if self.name in article:
                article_list.append(article)
        
        return article_list

    def contributors(self):
        article_list = []

        for article in Article.all:
            if self.name in article:
                article_list.append(article)
        print(article_list)
        author_list = []

        for article in article_list:
            author_list.append(article[0])
        print(author_list)
        unique_author_list = []

        for author in author_list:
            if author not in unique_author_list:
                unique_author_list.append(author)
        
        return unique_author_list

    def article_titles(self):
        article_list = []

        for article in Article.all:
            if self.name in article:
                article_list.append(article)

        return article_list
        
        # article_titles_for_magazine = []

        # for article in article_list:
        #     article_titles_for_magazine.append(article[2])

        # return article_titles_for_magazine

    def contributing_authors(self):
        pass