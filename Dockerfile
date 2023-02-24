FROM python:3.10

ENV PYTHONUNBUFFERED 1
ENV DJANGO_SECRETE_KEY django-insecure-v-7ao((8h@imx_hxsxvotehl##as#g1*!#e*mef=tho14b42)0
ENV STRIPE_PUBLIC_KEY pk_test_51MdpzMEWAtIZBkFYohmh8L8UZAr9XtCMv8yd3s1QH8LRcNXESILnfAU8gNtj430pxdOTMTjTXOD7QjjDY60iUD2s00cKnPbhcD
ENV STRIPE_SECRETE_KEY sk_test_51MdpzMEWAtIZBkFY0zqPxyOlygstr45yhOZ5GKIBAXQJ6ASShcauvAJ1PV6rfkQok6zmv8mYYjRoUyIrcFoOc8Ls007eRbEtos

WORKDIR /usr/src/djangostripe

COPY ./requirements.txt /usr/src/requirements.txt

RUN pip install -r /usr/src/requirements.txt

COPY . /usr/src/djangostripe

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
