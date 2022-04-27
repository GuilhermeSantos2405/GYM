from django.db import models
from stdimage import StdImageField


class Base(models.Model):
    criado = models.DateField('Data de criação', auto_now_add=True)
    modificado = models.DateField('Data de atualização', auto_now=True)
    ativo = models.BooleanField('Ativo', default=True)

    class Meta:
        abstract = True


class Profissao(Base):
    profissao = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.profissao


class Consultor(Base):
    nome = models.CharField('nome', max_length=100)
    sobrenome = models.CharField('sobrenome', max_length=100)
    profissao = models.ForeignKey(
        Profissao, on_delete=models.CASCADE, default=True)
    telefone = models.CharField(max_length=13)
    email = models.EmailField(max_length=255)
    descricao = models.TextField('descrição', max_length=255)
    imagem = StdImageField('Imagem', upload_to='media/img',
                           variations={'thumb': (124, 124)})

    def __str__(self):
        return self.nome


class Home(Base):
    titulo = models.CharField('titulo', max_length=100)
    descricao = models.TextField('descrição', max_length=255)
    imagem = StdImageField('Imagem', upload_to='media/suplementacao',
                           variations={'thumb': (1600, 776)})

    def __str__(self):
        return self.titulo


class Suplementacao(Base):
    titulo = models.CharField('titulo', max_length=100)
    descricao = models.TextField('descrição', max_length=255)
    imagem = StdImageField('Imagem', upload_to='media/suplementacao',
                           variations={'thumb': (1600, 776)})


class Dieta(Base):
    titulo = models.CharField('titulo', max_length=100)
    descricao = models.TextField('descrição', max_length=255)
    imagem = StdImageField('Imagem', upload_to='media/suplementacao',
                           variations={'thumb': (1600, 776)})


class Treinos(Base):
    titulo = models.CharField('titulo', max_length=100)
    descricao = models.TextField('descrição', max_length=255)
    imagem = StdImageField('Imagem', upload_to='media/suplementacao',
                           variations={'thumb': (1600, 776)})
