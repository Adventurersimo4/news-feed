import json
import requests
from bs4 import BeautifulSoup

class Article:
    "Article class"

def liverpool():
    Liverpool = Article()
    origin_url = "https://www.liverpool.com/liverpool-fc-news/"
    origin_soup = BeautifulSoup(requests.get(origin_url).content, features="lxml")
    articles = origin_soup.find("div",{"class":"pancake use-image-placeholders duet primary channel-liverpool-fc-news"})
    last_article = articles.find("div",{"class":"teaser"})
    link = last_article.find("a")["href"]
    header = last_article.find("a")["aria-label"]
    thumbnail = last_article.find("figure").find("a").find("img")["data-src"]
    topics = [str(last_article.find("div").find("a")).split(">")[1].split("<")[0]]
    Liverpool.link = link
    Liverpool.thumbnail = thumbnail
    Liverpool.header = header
    Liverpool.topics = topics
    return Liverpool

def mancity():
    ManCity = Article()
    origin_url = "https://www.mancity.com/news"
    origin_soup = BeautifulSoup(requests.get(origin_url).content, features="lxml")
    last_article = origin_soup.find("li",{"class":"news-list__item news-list__item--highlighted"})
    link = "https://www.mancity.com" + last_article.find("a")["href"]
    header = last_article.find("a").find("article")["aria-label"].strip("standardarticle: ")
    thumbnail = last_article.find("div",{"class":"mc-aspect-ratio-box mc-image-placeholder article-preview__figure-container"}).find("img")["src"]
    topics = [str(last_article.find("header",{"class":"article-preview__header-container"}).find("span")).split(">")[1].split("<")[0].strip()]
    ManCity.link = link
    ManCity.header = header
    ManCity.thumbnail = thumbnail
    ManCity.topics = topics
    return ManCity

def manu(): #FAILED
    ManU = Article()
    origin_url = "https://www.manutd.com/en/news/latest"
    origin_soup = BeautifulSoup(requests.get(origin_url).content, features="lxml")
    last_article = origin_soup.find("div",{"class":"main-container"}).find("div",{"data-module":"news-listing"}).find("section",{"class":"main"}).find("news-listing",{"id":"newslisting"}).find("div",{"class":"container main"}).find("div",{"class":"main_class grid-6 ratio child"})
    link = last_article.find("div",{"data-an-track":"true"}).find("a")["data-ng-href"]
    header = str(last_article.find("h2",{"class":"mu-item__title ng-binding ng-scope"})).split(">")[1].split("<")[0] + " - " + str(last_article.find("p",{"class":"mu-item__teasure ng-binding ng-scope"})).split(">")[1].split("<")[0]
    thumbnail = eval(last_article.find("figure",{"data-ng-if":"isNewslisting"})["style"].strip("background-image: url(").strip("; opacity: 1;"))
    ManU.link = link
    ManU.header = header
    ManU.thumbnail = thumbnail
    article = BeautifulSoup(requests.get(link).content, features="lxml")
    topics = [str(keyword.find("a")).split(">")[1].split("<")[0] for keyword in article.find("h2",{"class":"player-title"}).findAll("li")]
    ManU.topics = topics
    return ManU
    
def tottenham():
    Tottenham = Article()
    origin_url = "https://www.tottenhamhotspur.com/news/"
    origin_soup = BeautifulSoup(requests.get(origin_url).content, features="lxml")
    last_article = origin_soup.find("div",{"class":"TrendingGrid__16-9--left"})
    link = "https://www.tottenhamhotspur.com" + last_article.find("div",{"class":"TrendingGrid__16-9__container"}).find("div",{"class":"ArticleLink"}).find("div",{"class":"ArticleLink__info"}).findAll("a")[-1]["href"]
    header = str(last_article.find("div",{"class":"TrendingGrid__16-9__container"}).find("div",{"class":"ArticleLink"}).find("div",{"class":"ArticleLink__info"}).findAll("a")[-1]).split(">")[1].split("<")[0]
    thumbnail = last_article.find("div",{"class":"TrendingGrid__16-9__container"}).find("div",{"class":"ArticleLink"}).find("div",{"class":"ArticleLink__info"}).findAll("a")[:-1]
    topics = [str(raw_tag).split(">")[1].split("<")[0].strip("#") for raw_tag in last_article.find("div",{"class":"ArticleLink__tags"}).findAll("a")]
    Tottenham.link = link
    Tottenham.header = header
    Tottenham.thumbnail = thumbnail
    Tottenham.topics = topics
    return Tottenham

def leicester():
    Leicester = Article()
    origin_url = "https://www.lcfc.com/news"
    origin_soup = BeautifulSoup(requests.get(origin_url).content, features="lxml")
    last_article = origin_soup.find("section",{"data-widget":"content-list"}).find("li").find("div",{"class":"thumbnail thumbnail--hero poly-object-fit js-article-expand"}).find("figure")
    link = "https://www.lcfc.com" + last_article.find("a")["href"]
    header = str(last_article.find("figcaption").find("div",{"class":"thumbnail__text"}).find("a")).split(">")[1].split("<")[0]
    thumbnail = last_article.find("a").find("picture").find("img")["src"]
    topics = [str(last_article.find("figcaption").find("div",{"class":"thumbnail__meta"}).find("div",{"class":"thumbnail__category"})).split(">")[1].split("<")[0]]
    Leicester.link = link
    Leicester.header = header
    Leicester.thumbnail = thumbnail
    Leicester.topics = topics
    return Leicester

def chelsea():
    Chelsea = Article()
    origin_url = "https://www.chelseafc.com/en/news"
    origin_soup = BeautifulSoup(requests.get(origin_url).content, features="lxml")
    last_article = origin_soup.find("div",{"class":"news-sections ng-star-inserted"}).find("cfc-news-article-tile")
    link = "https://www.chelseafc.com/" + last_article.find("a")["href"]
    header = str(last_article.find("a").find("b").find("article").find("div",{"class":"tile__description"}).find("h3")).split(">")[1].split("<")[0]
    thumbnail = "https://res.cloudinary.com/chelsea-production/image/upload/c_fill,dpr_2.0,f_auto,fl_lossy,g_auto,h_96,q_auto,w_96,z_1.0/v1/logos/rgb-mar18.png"
    topics = [str(last_article.find("a").find("b").find("article").find("div",{"class":"tile__type ng-star-inserted"}).find("span")).split(">")[1].split("<")[0]]
    Chelsea.link = link
    Chelsea.header = header
    Chelsea.thumbnail = thumbnail
    Chelsea.topics = topics
    return Chelsea

def arsenal():
    Arsenal = Article()
    origin_url = "https://www.arsenal.com/news"
    origin_soup = BeautifulSoup(requests.get(origin_url).content, features="lxml")
    last_article = origin_soup.find("div",{"class":"accordion__content"}).find("a",{"class":"article-card__wrapper"})
    link = "https://www.arsenal.com" + last_article["href"]
    header = last_article.find("div",{"class":"article-card__content"}).find("h3",{"class":"article-card__title"})["title"]
    thumbnail = last_article.find("div",{"class":"article-card__media"}).find("div",{"aria-role":"img"})["data-src"]
    topics = [str(last_article.find("div",{"class":"article-card__content"}).find("span")).split(">")[1].split("<")[0]]
    Arsenal.link = link
    Arsenal.header = header
    Arsenal.thumbnail = thumbnail
    Arsenal.topics = topics
    return Arsenal

def everton():
    Everton = Article()
    origin_url = "https://www.evertonfc.com/news"
    origin_soup = BeautifulSoup(requests.get(origin_url).content, features="lxml")
    last_article = origin_soup.find("section",{"class":"match-list-wrapper"}).find("ol",{"class":"article-list article-list--no-sidebar js-list"}).find("li",{"class":"article-list__item"})
    link = "https://www.evertonfc.com" + last_article.find("a")["href"]
    header = last_article.find("a")["title"]
    thumbnail = last_article.find("header",{"class":"media-thumbnail__image-container"}).find("div")["data-desktop-img"]
    article = BeautifulSoup(requests.get(link).content, features="lxml")
    topics = [str(raw_tag).split(">")[1].split("<")[0] for raw_tag in article.find("div",{"class":"article__tags-wrapper"}).findAll("span")]
    Everton.link = link
    Everton.header = header
    Everton.thumbnail = thumbnail
    Everton.topics = topics
    return Everton

def westham():
    WestHam = Article()
    origin_url = "https://www.whufc.com/news/latest-news"
    origin_soup = BeautifulSoup(requests.get(origin_url).content, features="lxml")
    last_article = origin_soup.find("section",{"class":"col-md-9 col-sm-8 col-xs-12"}).find("div",{"class":"region region-content"}).find("div",{"class":"views-element-container form-group"}).find("div",{"class":"view view-news-articles-view view-id-news_articles_view view-display-id-latest_news_view js-view-dom-id-19b311636a4dfe9a7fd81cce3283c328b63be84e24a2c7b6cebb6df630aa3fbf"}).find("div",{"class":"view-content"}).find("div",{"class":"views-infinite-scroll-content-wrapper clearfix form-group"})
    link = "https://www.whufc.com" + last_article.find("a")["href"]
    header = str(last_article.find("div",{"class":"news-content"}).find("div",{"class":"news-title"})).split(">")[1].split("<")[0]
    thumbnail = "https://www.whufc.com" + last_article.find("div",{"class":"news-content"}).find("div",{"class":"news-image"}).find("img")["src"]
    topics = [str(last_article.find("div",{"class":"news-content"}).find("div",{"class":"news-category"})).split(">")[1].split("<")[0]]
    WestHam.link = link
    WestHam.header = header
    WestHam.thumbnail = thumbnail
    WestHam.topics = topics
    return WestHam

def astonvilla(): #FAILED
    AstonVilla = Article()
    origin_url = "https://www.avfc.co.uk/news"
    origin_soup = BeautifulSoup(requests.get(origin_url).content, features="lxml")
    last_article = origin_soup.find("div",{"class":"news-grid__items standard-four"}).find("article").find("div",{"class":"grid-card__wrap"}).find("a")
    link = "https://www.whufc.com" + last_article["href"]
    header = str(last_article.find("h3",{"class":"grid-card__title h5"})).split(">")[1].split("<")[0]
    thumbnail = eval(origin_soup.find("div",{"class":"news-grid__items standard-four"}).findAll("article")[3]["style"].split("url")[1].strip(";"))
    topics = [str(last_article.find("div",{"class":"grid-card__meta"}).find("p",{"class":"grid-card__category"})).split(">")[1].split("<")[0]]
    AstonVilla.link = link
    AstonVilla.header = header
    AstonVilla.thumbnail = thumbnail
    AstonVilla.topics = topics
    return AstonVilla

def wolves():
    Wolverhampton = Article()
    origin_url = "https://www.wolves.co.uk/news/"
    origin_soup = BeautifulSoup(requests.get(origin_url).content, features="lxml")
    last_article = origin_soup.find("div",{"class":"container js-load-more"}).find("article").find("a")
    link = "https://www.wolves.co.uk/news" + last_article["href"]
    header = str(last_article.find("span",{"class":"card__title"})).split(">")[1].split("<")[0]
    thumbnail = last_article.find("div",{"class":"card--image"}).find("picture").find("source")["srcset"]
    topics = [str(last_article.find("div",{"class":"card--content"}).find("div",{"class":"card--category"})).split(">")[1].split("<")[0]]
    Wolverhampton.link = link
    Wolverhampton.header = header
    Wolverhampton.thumbnail = thumbnail
    Wolverhampton.topics = topics
    return Wolverhampton

def leeds():
    Leeds = Article()
    origin_url = "https://www.leedsunited.com/news"
    origin_soup = BeautifulSoup(requests.get(origin_url).content, features="lxml")
    last_article = origin_soup.find("div",{"class":"full-news"}).find("div",{"class":"row"})
    link = last_article.find("div",{"class":"col-md-6 text-news"}).find("header").find("a")["href"]
    header = str(last_article.find("div",{"class":"col-md-6 text-news"}).find("header").find("a").find("h2")).split(">")[1].split("<")[0]
    thumbnail = last_article.find("div",{"class":"col-md-6 news-image"}).find("figure").find("img")["src"]
    topics = []
    Leeds.link = link
    Leeds.header = header
    Leeds.thumbnail = thumbnail
    Leeds.topics = topics
    return Leeds

def southampton(): #FAILED
    Southampton = Article()
    origin_url = "https://www.southamptonfc.com"
    origin_soup = BeautifulSoup(requests.get(origin_url).content, features="lxml")
    last_article = origin_soup.find("div",{"class":"content"}).find("section",{"class":"main"})#.find("div",{"class":"saints-live"}).find("div",{"class":"newsfeed js-filterable-list"}).find("div",{"class":"newsfeed__content content__inner"}).find("div",{"class":"list js-filterable-item"})
    link = "https://www.southamptonfc.com" + last_article.find("div",{"data-category":"standard"}).find("a")["href"]
    header = last_article.find("div",{"class":"card__thumb"}).find("img")["alt"]
    thumbnail = last_article.find("div",{"class":"card__thumb"}).find("img")["src"]
    topics = [str(last_article.find("div",{"data-category":"standard"}).find("a").find("div",{"class":"card__content"}).find("div",{"class":"tag"})).split(">")[1].split("<")[0]]
    Southampton.link = link
    Southampton.header = header
    Southampton.thumbnail = thumbnail
    Southampton.topics = topics
    return Southampton

def crystalpalace():
    CrystalPalace = Article()
    origin_url = "https://www.cpfc.co.uk/news/latest-news/"
    origin_soup = BeautifulSoup(requests.get(origin_url).content, features="lxml")
    last_article = origin_soup.find("div",{"class":"row article-filtered-container article-grid-container"}).find("div",{"class":"col-sm-3 col-xs-12 article-container"})
    link = "https://www.cpfc.co.uk" + last_article.find("a")["href"]
    header = str(last_article.find("div",{"class":"article-panel match-height"}).find("div",{"class":"news-detail-wrap"}).find("h3")).split(">")[1].split("<")[0]
    thumbnail = last_article.find("div",{"class":"image-container"}).find("img")["src"]
    topics = [str(last_article.find("div",{"class":"article-panel match-height"}).find("div",{"class":"news-detail-wrap"}).find("span",{"class":"category detail"})).split(">")[1].split("<")[0]]
    CrystalPalace.link = link
    CrystalPalace.header = header
    CrystalPalace.thumbnail = thumbnail
    CrystalPalace.topics = topics
    return CrystalPalace

def burnley(): #FAILED
    Burnley = Article()
    origin_url = "https://www.burnleyfootballclub.com/news/"
    origin_soup = BeautifulSoup(requests.get(origin_url).content, features="lxml")
    last_article = origin_soup.find("div",{"class":"container"}).find("div",{"class":"flex"}).find("div",{"class":"w-full"}).find("div",{"class":"mb-4"})
    link = "https://www.cpfc.co.uk" + last_article.find("div",{"class":"flex-1"}).find("div",{"class":"vertical-card-image"})["src"]
    header = last_article.find("div",{"class":"vertical-card-image overflow-hidden relative"}).find("img")["alt"]
    thumbnail = last_article.find("div",{"class":"vertical-card-image overflow-hidden relative"}).find("img")["src"]
    topics = [str(last_article.find("div",{"class":"article-panel match-height"}).find("div",{"class":"news-detail-wrap"}).find("span",{"class":"category detail"})).split(">")[1].split("<")[0]]
    Burnley.link = link
    Burnley.header = header
    Burnley.thumbnail = thumbnail
    Burnley.topics = topics
    return Burnley

def brighton(): #FAILED
    BrightonHoveAlbion = Article()
    origin_url = "https://www.brightonandhovealbion.com/news?type=-1"
    origin_soup = BeautifulSoup(requests.get(origin_url).content, features="lxml")
    last_article = origin_soup.find("div",{"class":"wrapper"}).find("div",{"class":"row"}).find("section",{"class":"news-listing"}).find("div",{"class":"js-news-list"}).find("ul").find("li")
    link = "https://www.brightonandhovealbion.com/" + last_article.find("a")["href"]
    header = last_article.find("a")["title"]
    thumbnail = last_article.find("a").find("div",{"class":"content-item__thumbnail"}).find("div",{"class":"lazy-image__container"})["data-src"]
    topics = [str(last_article.find("div",{"class":"content-item__content"}).find("div",{"class":"content-item__content-inner"}).find("p",{"class":"content-item__detail"}).find("span")).split(">")[1].split("<")[0]]
    BrightonHoveAlbion.link = link
    BrightonHoveAlbion.header = header
    BrightonHoveAlbion.thumbnail = thumbnail
    BrightonHoveAlbion.topics = topics
    return BrightonHoveAlbion

def newcastle():
    NewcastleUtd = Article()
    origin_url = "https://www.nufc.co.uk/news/"
    origin_soup = BeautifulSoup(requests.get(origin_url).content, features="lxml")
    last_article = origin_soup.find("div",{"id":"main"}).find("section").find("div",{"class":"centered-content"}).find("a",{"class":"hero-card__wrapperLink"})
    link = last_article["href"]
    header = str(last_article.find("div",{"class":"hero-card__content"}).find("h2",{"class":"hero-card__title"})).split(">")[1].split("<")[0]
    thumbnail = last_article.find("div",{"class":"hero-card__img"}).find("figure").find("img")["data-src"]
    topics = [str(last_article.find("div",{"class":"hero-card__content"}).find("p",{"class":"hero-card__cat"})).split(">")[1].split("<")[0]]
    NewcastleUtd.link = link
    NewcastleUtd.header = header
    NewcastleUtd.thumbnail = thumbnail
    NewcastleUtd.topics = topics
    return NewcastleUtd

def sheffield():
    SheffieldUtd = Article()
    origin_url = "https://www.sufc.co.uk/news"
    origin_soup = BeautifulSoup(requests.get(origin_url).content, features="lxml")
    last_article = origin_soup.find("section",{"class":"container"}).find("div",{"class":"news-grid__wrap"}).find("article")
    link = "https://www.sufc.co.uk" + last_article.find("a")["href"]
    header = str(last_article.find("div").find("h3")).split(">")[1].split("<")[0]
    thumbnail = "https://www.sufc.co.uk/logo.png"
    topics = [str(last_article.find("a").find("div").find("p")).split(">")[1].split("<")[0]]
    SheffieldUtd.link = link
    SheffieldUtd.header = header
    SheffieldUtd.thumbnail = thumbnail
    SheffieldUtd.topics = topics
    return SheffieldUtd

def fulham():
    Fulham = Article()
    origin_url = "https://www.fulhamfc.com/news"
    origin_soup = BeautifulSoup(requests.get(origin_url).content, features="lxml")
    last_article = origin_soup.find("section",{"class":"container"}).find("div",{"class":"news-grid__wrap"}).find("article")
    link = "https://www.fulhamfc.com" + last_article.find("a")["href"]
    header = str(last_article.find("div").find("h3")).split(">")[1].split("<")[0]
    thumbnail = "https://upload.wikimedia.org/wikipedia/en/thumb/e/eb/Fulham_FC_(shield).svg/1200px-Fulham_FC_(shield).svg.png"
    topics = [str(last_article.find("a").find("div").find("p")).split(">")[1].split("<")[0]]
    Fulham.link = link
    Fulham.header = header
    Fulham.thumbnail = thumbnail
    Fulham.topics = topics
    return Fulham

def westbrom():
    WestBromwichAlbion = Article()
    origin_url = "https://www.wba.co.uk/news"
    origin_soup = BeautifulSoup(requests.get(origin_url).content, features="lxml")
    last_article = origin_soup.find("div",{"class":"layout-content"}).find("div",{"class":"o-news__listing"}).find("div",{"class":"o-news__item"}).find("article")
    link = "https://www.wba.co.uk" + last_article.find("a")["href"]
    header = str(last_article.find("a").find("span")).split(">")[1].split("<")[0].strip()
    thumbnail = last_article.find("div",{"class":"m-teaser__thumbnail"}).find("img")["data-src"]
    topics = [str(last_article.find("div",{"class":"m-teaser__content"}).find("span",{"class":"ff-brush category"}).find("a")).split(">")[1].split("<")[0]]
    WestBromwichAlbion.link = link
    WestBromwichAlbion.header = header
    WestBromwichAlbion.thumbnail = thumbnail
    WestBromwichAlbion.topics = topics
    return WestBromwichAlbion