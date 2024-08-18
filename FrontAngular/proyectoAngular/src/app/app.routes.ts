import { Routes } from '@angular/router';
import { ListarComponent } from './Usuarios/listar/listar.component';
import { AddComponent } from './Usuarios/add/add.component';
import { EditComponent } from './Usuarios/edit/edit.component';

export const routes: Routes = [
    {path:'listar',component:ListarComponent},
    {path:'add',component:AddComponent},
    {path:'edit',component:EditComponent},
];
