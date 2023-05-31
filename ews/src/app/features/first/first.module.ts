import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FirstComponent } from './first.component';
import { FooterModule } from '@patterns/footer';
import { CardModule } from '@patterns/card';
import { SidebarComponent } from '../sidebar/sidebar.component';
import { SidebarModule } from '../sidebar/sidebar.module';

@NgModule({
  declarations: [FirstComponent],
  imports: [
    CommonModule,
    FooterModule,
    CardModule,
    SidebarModule
  ],
  exports: [FirstComponent],
})
export class FirstModule {}
