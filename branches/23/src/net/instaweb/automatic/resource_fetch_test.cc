/*
 * Copyright 2012 Google Inc.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

// Author: morlovich@google.com (Maksim Orlovich)

// Unit-tests for ResourceFetch

#include "net/instaweb/automatic/public/resource_fetch.h"

#include "net/instaweb/htmlparse/public/html_parse_test_base.h"
#include "net/instaweb/http/public/content_type.h"
#include "net/instaweb/http/public/sync_fetcher_adapter_callback.h"
#include "net/instaweb/http/public/wait_url_async_fetcher.h"
#include "net/instaweb/rewriter/public/rewrite_test_base.h"
#include "net/instaweb/rewriter/public/rewrite_options.h"
#include "net/instaweb/rewriter/public/server_context.h"
#include "net/instaweb/rewriter/public/test_rewrite_driver_factory.h"
#include "net/instaweb/util/public/function.h"
#include "net/instaweb/util/public/google_url.h"
#include "net/instaweb/util/public/gtest.h"
#include "net/instaweb/util/public/mock_scheduler.h"
#include "net/instaweb/util/public/mock_timer.h"
#include "net/instaweb/util/public/string.h"
#include "net/instaweb/util/public/string_writer.h"

namespace net_instaweb {

namespace {

const char kCssContent[] = "* { display: none; }";
const char kMinimizedCssContent[] = "*{display:none}";

class ResourceFetchTest : public RewriteTestBase {
};

TEST_F(ResourceFetchTest, BlockingFetch) {
  SetResponseWithDefaultHeaders("a.css", kContentTypeCss, kCssContent, 100);

  // Make this actually happen asynchronously.
  SetupWaitFetcher();
  mock_scheduler()->AddAlarm(
      mock_timer()->NowUs() + 100,
      MakeFunction(factory()->wait_url_async_fetcher(),
                   &WaitUrlAsyncFetcher::CallCallbacks));

  // Now fetch stuff.
  GoogleString buffer;
  StringWriter writer(&buffer);
  SyncFetcherAdapterCallback* callback =
      new SyncFetcherAdapterCallback(server_context()->thread_system(),
                                     &writer);
  RewriteOptions* custom_options =
      server_context()->global_options()->Clone();
  RewriteDriver* custom_driver =
      server_context()->NewCustomRewriteDriver(custom_options);

  GoogleUrl url(Encode(kTestDomain, "cf", "0", "a.css", "css"));
  EXPECT_TRUE(
      ResourceFetch::BlockingFetch(
          url, server_context(), custom_driver, callback));
  EXPECT_TRUE(callback->done());
  EXPECT_TRUE(callback->success());
  callback->Release();

  EXPECT_EQ(kMinimizedCssContent, buffer);
}

}  // namespace

}  // namespace net_instaweb