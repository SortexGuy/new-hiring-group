from __future__ import annotations
import rio
import httpx
from .. import SERVER_URL


@rio.page(
    name='Sample Page 2',
    url_segment='v2',
)
class SamplePage2(rio.Component):
    """
    This is an example Page. Pages are identical to other Components and only
    differ in how they're used.
    """

    async def get_users_button_hdlr(self):
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(f'{SERVER_URL}dj/api/usuarios/')
                print(response.headers)
                if response.status_code == 200:
                    data = response.json()
                    print(data)
                    # self.tasks = [Task(**task) for task in data]
        except Exception as e:
            print(f'Error loading tasks: {e}')
        finally:
            self.loading = False
        pass

    def build(self) -> rio.Component:
        return rio.Column(
            rio.Text('My App', style='heading2'),
            rio.Button('Get Users', on_press=self.get_users_button_hdlr),
            spacing=2,
            margin=2,
            align_x=0.5,
            align_y=0,
        )
