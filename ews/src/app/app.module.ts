import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { ElementModule } from '@patterns/element';
import { ContentModule } from '@patterns/content';
import { ButtonModule } from '@patterns/button';
import { CardModule } from '@patterns/card';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { TranslateLoader, TranslateModule } from '@ngx-translate/core';
import { TranslateHttpLoader } from '@ngx-translate/http-loader';

export function createTranslateLoader(http: HttpClient) {
  return new TranslateHttpLoader(http, './assets/i18n/', '.json');
}

@NgModule({
  declarations: [AppComponent],
  providers: [],
  bootstrap: [AppComponent],
  imports: [
    ContentModule,
    ElementModule,
    ButtonModule,
    CardModule,
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    BrowserAnimationsModule,
    TranslateModule.forRoot({
      extend: true,
      defaultLanguage: 'en',
      loader: {
        provide: TranslateLoader,
        deps: [HttpClient],
        useFactory: createTranslateLoader,
      },
    }),
  ],
  exports: [TranslateModule],
})
export class AppModule {}
