from .models import additional

def addition(request):
	add = additional.objects.all().first()
	return {'add': add}

def gnb_menus(request):
	menus = [
		{
			'name': '대시보드',
			'url': '/dashboard/'
		},{
			'name': '제품별 현황',
			'url': '/product/1',
			'sub_menus': [
				{'name': 'SecuMS', 'url': '/product/1'},
				{'name': 'OmniGuard Unix', 'url': '/product/2'},
				{'name': 'OmniGuard Windows', 'url': '/product/3'},
				{'name': 'FOSSGuard', 'url': '/product/4'},
				{'name': 'Athena', 'url': '/product/5'},
			]
		},
		{
			'name': '기능 자동화',
			'url': '/functionauto/'
		},
		{
			'name': '품질 분석실',
			'url': '/analysis/'
		},
		{
			'name': '로그 모니터링',
			'url': '/logmonitor/'
		},
		{
			'name': '성능 모니터링',
			'url': '/logperform/'
		},
		{
			'name': '품질 자동화',
			'url': '/qualityauto/'
		},
		{
			'name': '품질 자동화',
			'url': '/logperform/'
		},
		{
			'name': '품질 자동화',
			'url': '/logperform/'
		}
	]
	return {'gnb_menus': menus}