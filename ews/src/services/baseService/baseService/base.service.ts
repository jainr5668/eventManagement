import {
  HttpClient,
  HttpResponse,
  HttpErrorResponse,
  HttpHeaders,
} from '@angular/common/http';
import { catchError, map } from 'rxjs/operators';
import { of, Observable } from 'rxjs';

export class BaseService<T> {
  /**
   * Make HTTP client available to child classes
   */
  public http: HttpClient | undefined;
}
