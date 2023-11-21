## 1. nickname 불러오기
- 로그인 후 닉네임을 불러오려고 했으나, rest_auth를 이용해 login을 진행 한 경우 return 되는 항목이 토큰 외에 다른것은 찾을 수 없었음.
### 시도해본 것들
- 기존에 배포받은 pdf파일에 들어있는 내용처럼 git hub에 들어가 login 항목들을 찾아보고 커스텀을 시도해 보려 했으나 실패
    - 한시간 정도 잡고 시도해 보려 했으나 rest_auth에 있는 방식은 단순히 함수를 불러오는 것이 아니라 class를 호출하여
    진행하는 방식이어서 익숙하지 않았음.
    - class 내부에 있는 로그인 함수가 serializer를 참조해와서 사용하고 있었지만 rest_auth 역시 django의 몇몇 기본 기능을
    상속받아 사용하고 있어서 git hub 자체에서는 확인이 불가능 했음.
- url을 살펴보는 와중 로컬 파일에 있는 항목을 수정하여 커스텀 하려고 했으나 시도하지 않음
    - venv는 ignore 에 작성되어 있어서 로컬에서만 수정이 가능하고 rest_auth만 ignore 리스트에서 지워서 작업하기엔 번거로워 질 것 같고, 시간을 더 많이 소요 할 것으로 예상되어 시도하지 않았다.
- final-pjt-back/urls.py 에 직접 url을 작성하고 accounts/views.py에 함수를 작성하여 호출 해 시도
    ```
    Internal Server Error: /getuserinfo/user10/
    Traceback (most recent call last):
    File "C:\Users\44968\OneDrive\바탕 화면\Flicks-on\back\venv\lib\site-packages\django\core\handlers\exception.py", line 55, in inner
        response = get_response(request)
    File "C:\Users\44968\OneDrive\바탕 화면\Flicks-on\back\venv\lib\site-packages\django\core\handlers\base.py", line 197, in _get_response
        response = wrapped_callback(request, *callback_args, **callback_kwargs)
    File "C:\Users\44968\OneDrive\바탕 화면\Flicks-on\back\accounts\views.py", line 13, in get_user_info
        return Response(serializer.data)
    File "C:\Users\44968\OneDrive\바탕 화면\Flicks-on\back\venv\lib\site-packages\rest_framework\serializers.py", line 555, in data
        ret = super().data
    File "C:\Users\44968\OneDrive\바탕 화면\Flicks-on\back\venv\lib\site-packages\rest_framework\serializers.py", line 253, in data
        self._data = self.to_representation(self.instance)
    File "C:\Users\44968\OneDrive\바탕 화면\Flicks-on\back\accounts\serializers.py", line 43, in to_representation
        ret = super().to_representation(instance)
    File "C:\Users\44968\OneDrive\바탕 화면\Flicks-on\back\venv\lib\site-packages\rest_framework\serializers.py", line 522, in to_representation
        ret[field.field_name] = field.to_representation(attribute)
    File "C:\Users\44968\OneDrive\바탕 화면\Flicks-on\back\venv\lib\site-packages\rest_framework\fields.py", line 915, in to_representation
        return int(value)
    TypeError: int() argument must be a string, a bytes-like object or a number, not 'DeferredAttribute'
    ```
    
    - 다음과 같은 오류 발생
    - age 필드가 비어 있어서 발생한 오류로 추정
    - user의 serializer를 다음과 같이 수정
    ```python
    class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('nickname', )
    ```
    ```
    Internal Server Error: /getuserinfo/user10/
    Traceback (most recent call last):
    File "C:\Users\44968\OneDrive\바탕 화면\Flicks-on\back\venv\lib\site-packages\django\core\handlers\exception.py", line 55, in inner
        response = get_response(request)
    File "C:\Users\44968\OneDrive\바탕 화면\Flicks-on\back\venv\lib\site-packages\django\core\handlers\base.py", line 220, in _get_response
        response = response.render()
    File "C:\Users\44968\OneDrive\바탕 화면\Flicks-on\back\venv\lib\site-packages\django\template\response.py", line 114, in render
        self.content = self.rendered_content
    File "C:\Users\44968\OneDrive\바탕 화면\Flicks-on\back\venv\lib\site-packages\rest_framework\response.py", line 55, in rendered_content
        assert renderer, ".accepted_renderer not set on Response"
    AssertionError: .accepted_renderer not set on Response
    ```

    - 다른 오류 발생 &rarr; api_view 데코레이터를 달지 않아서 발생했던 오류 였음( 해결 )
    - serializer를 통해 리턴한 객체에 nickname 값이 다음과 같이 출력
        ```
        nickname: "<django.db.models.query_utils.DeferredAttribute object at 0x000001EC196FFA60>"
        ```
    - rest_auth 를 이용해 signup과 login을 진행해 발생한 오류로 추정 django에서 print로 확인했을 때도 동일하게 출력
    - rest_auth의 login 함수를 커스텀 해야 할 것으로 보임 &rarr; 첫 번째 방식으로 돌아갈 듯
- rest_auth의 LoginView class 를 상속받는 CustomLoginView 클래스 작성해서 시도
    - view 함수에 다음과 같이 작성
    ```python
    class CustomLoginView(LoginView):

        def login(self, request):
            self.user = self.serializer.validated_data['user']
            token_model = get_token_model()

            if api_settings.USE_JWT:
                self.access_token, self.refresh_token = jwt_encode(self.user)
            elif token_model:
                self.token = api_settings.TOKEN_CREATOR(token_model, self.user, self.serializer)

            if api_settings.SESSION_LOGIN:
                self.process_login()

            response_data = {
                'token': self.token,
                'user_id': self.user.pk,
                'username': self.user.username,
            }

            return self.get_response(request, response_data=response_data)
    ```
    - urls.py 수정
    ```python
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('api/v1/', include('movies.urls')),
        path('login/', views.CustomLoginView.as_view()),
        path('accounts/', include('dj_rest_auth.urls')),
        path('accounts/signup/', include('dj_rest_auth.registration.urls')),
    ]
    ```
    - TypeError: login() missing 1 required positional argument: 'request' 오류 발생 &rarr; request 제거
    - TypeError: get_response() got an unexpected keyword argument 'response_data' 오류 발생 &rarr; request 추가
    - get_response에만 request를 추가하면 없는 인자를 추가한 것 이어서 안댐
    - rest_auth login 함수에는 request가 없는데 잘 동작 하는데 어떻게 한건지 모르겠다.
    - 여러번의 시도 끝에 view 함수 안에 있는 serializer에 username, email, password만 들어있는걸 찾아냄 serializer를 수정해야된 다는 사실을 깨달음
    - registration 을 커스텀 했던 것 처럼 커스텀 해야 함
    - 기존에 serializer를 호출 하던 방식에서 내가 커스텀한 serializer를 넣는다.
    - 너무 많은걸 바꿔야 할 것 같아서 이건 아닌거 같다.
    - self.serializer 항목을 전부 Custom serializer로 바꿔주려 했지만 기존에 존재하는 serializer의 어떤 부분을 수정해야 하는지 모르겠다.
- 공식문서를 찾으면서 user detail을 불러 올 수 있는 url 발견
    - serializer를 custom 하고 settings 에 추가해 주니까 성공적으로 return 했다.
    - 공식문서에 따르면 put 요청 역시 이것을 통해 하면 된다고 명시되어 있음.
- 작성자 : 박수형


## 2. MovieList Components 에 원하는 Props 를 내려받아 영화 불러오기
- `MainView` &rarr; `MovieList` Components, `MovieDetailView` &rarr; `MovieList` Components 에서 원하는 Movie 정보에 따라 다른 `Props` 를 내려주고 싶었다. 

### 시도해본 것들
- 코드 1
   ```
   import { useMovieStore } from '@/stores/movies'
   
   const movieStore = useMovieStore()
   movieStore.getNowPlayingMovie()
   const nowPlayingMovieList = movieStore.nowPlayingMovie
   console.log(nowPlayingMovieList)
   ```

- 코드 2
   ```   
   import { useMovieStore } from '@/stores/movies'
   
   const movieStore = useMovieStore()
   const nowPlayingMovieList = ref([])
   onBeforeMount(async () => {
     await movieStore.getNowPlayingMovie()
      nowPlayingMovieList.value = await movieStore.nowPlayingMovie
   })
   ```

- 코드 3
   ```
   import { useMovieStore } from '@/stores/movies'

   const movieStore = useMovieStore()
   const nowPlayingMovieList = ref([])
   const isDataLoaded = ref(false)
   onMounted(async () => {
     try {
       await movieStore.getNowPlayingMovie()
       nowPlayingMovieList.value = movieStore.nowPlayingMovie

       isDataLoaded.value = true
     } catch (error) {
       console.error('Error fetching movie list:', error)
     }
   })
   ```

- 이외에도 여러 가지 방식으로 코드를 작성해보았으나, 모든 코드가 동작은 되지만 비동기 처리로 인해 첫 렌더링 때 영화를 불러오지 못했다. (메인 &rarr; 다른 페이지로 이동했다가 뒤로 가기하면 재렌더링될 때는 로딩이 됨)
- 페이지 첫 렌더링과 데이터 로딩 비동기 처리에 대해 고민해보았으나 성공하지 못하고, 다른 방식으로 코드 작성을 완료하였다.
- 결국, 다른 데이터를 가지고 있는 똑같은 컴포넌트를 여러 개 만들었다.
- `MovieListNowPlaying` Component, `MovieListTopRated` Component, `MoviesListSimilar` Component
- 작성자 : 전소현

## 3. MovieList Components 에 원하는 Props 를 내려받아 영화 불러오기
    ```
        @click="goPage('movie_detail', movie.id)"
    ```
- `MovieList` Components &rarr; `MovieDetailView` &rarr; `MovieDetail` Components, `MovieListSimilar` Components 로 연결된다.
- `MovieListSimilar` Components 에서 `MovieDetailView` 를 다시 불러오는 과정에서, 새로운 영화들의 데이터를 가져오고 싶었다.

### 시도해본 것들

- 코드 1.
    ```
   const goPage = function (pageName, id) {
     router.push({name: pageName, params: {title: id}})
     router.go(0)
   }
   ```

- 코드 2.
    ```
   const goPage = function (pageName, id) {
      네비게이션 가드에서 디버깅을 위해 훅을 추가
     router.beforeEach((to, from, next) => {
       console.log('Before route update', { to, from });
       next();
     });
     router.push({ name: pageName, params: { title: id } });
   }
    ```

- 코드 3.
    ```
   const goPage = function (pageName, id, forceReload = false) {
     if (forceReload) {
       window.location.href = `#/${pageName}/${id}`
     } else {
       router.push({name: pageName, params: {title: id}})
     }
   }
    ```

- 코드 4.
    ```
   const goPage = function (pageName, id) {
     router.go({name: pageName, params: {title: id}, replace: true})
   }
    ```

- 코드 5.
    ```
   const goPage = function (pageName, id) {
     router.replace({name: pageName, params: {title: id}})
   }
    ```

- 코드 6.
    ```
   const goPage = function (pageName, id) {
     router.replace({name: pageName, params: {title: id}})
     window.location.reload()
   }
    ```

- 코드 7
    ```
   const goPage = function (pageName, id) {
     router.push({name: pageName, params: {title: id}, replace: true})
   }
    ```

- 코드 8
    ```
   const goPage = function (pageName, id) {
     router.replace({name: pageName, params: {newId: id}})
   }
    ```

- page url 이 변경되지만, 같은 route 의 다른 variable routing 의 route 로는 컴포넌트가 새로고침이 되지 않았다.
- 작성자 : 전소현