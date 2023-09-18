from shortener.models import URL


def test_representation_url_str(sample_url):
    assert str(sample_url) == "http://www.example.com -> A4PKXTx5VKTjE4BnM6EkuL"


def test_representation_long_url_str(sample_long_url):
    assert str(sample_long_url) == "https://pytest-django.readthed -> RoFXW9P2T4vQFsLPqcVBU4"
    assert len(str(sample_long_url).split()[0]) == 30


def test_creation_url(sample_url):
    assert sample_url.created_at is not None
    assert sample_url.pk is not None
    assert sample_url.url == "http://www.example.com"
    assert sample_url.short_url == "A4PKXTx5VKTjE4BnM6EkuL"


def test_mirroring_url(db):
    url1 = URL.objects.create(
        url="http://www.example1.com",
        short_url="example1",
    )

    url2 = URL.objects.create(
        url="http://www.example1.com",
        short_url="example1",
    )

    assert URL.objects.get(url="http://www.example1.com").created_at == url1.created_at
    assert URL.objects.filter(url="http://www.example1.com").count() == 1
