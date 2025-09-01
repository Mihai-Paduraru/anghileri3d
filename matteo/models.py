from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titolo")
    description = models.TextField(verbose_name="Descrizione")
    image = models.ImageField(upload_to='projects/', verbose_name="Immagine")
    url = models.URLField(blank=True, verbose_name="URL del progetto")
    github_url = models.URLField(blank=True, verbose_name="URL GitHub")
    technologies = models.CharField(max_length=200, verbose_name="Tecnologie")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data di creazione")
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Progetto"
        verbose_name_plural = "Progetti"


class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nome")
    email = models.EmailField(verbose_name="Email")
    message = models.TextField(verbose_name="Messaggio")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data di invio")
    is_read = models.BooleanField(default=False, verbose_name="Letto")
    
    def __str__(self):
        return f"{self.name} - {self.email}"
    
    class Meta:
        verbose_name = "Messaggio di contatto"
        verbose_name_plural = "Messaggi di contatto"